# Convert 'quote_datetime' to datetime format
df_train['quote_datetime'] = pd.to_datetime(df_train['quote_datetime'])
df_test['quote_datetime'] = pd.to_datetime(df_test['quote_datetime'])

# Convert 'quote_datetime' to Unix timestamp
df_train['quote_datetime'] = df_train['quote_datetime'].astype(int) / 10**9
df_test['quote_datetime'] = df_test['quote_datetime'].astype(int) / 10**9

# Define features and target variable for the training dataset
X_train = df_train.drop(columns=['realized_return_variance'])
y_train = df_train['realized_return_variance']

# Define features and target variable for the testing dataset
X_test = df_test.drop(columns=['realized_return_variance'])
y_test = df_test['realized_return_variance']

# Display the first few rows of the updated datasets
X_train.head(), y_train.head(), X_test.head(), y_test.head()


from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import torch
from torch import nn, optim

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Define a function to compute R^2 score
def compute_r2_score(y_true, y_pred):
    return r2_score(y_true, y_pred)

# Define a function to train and evaluate a model
def train_and_evaluate_model(model, X_train, y_train, X_test, y_test):
    # Train the model
    model.fit(X_train, y_train)
    
    # Make predictions
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    
    # Compute R^2 score
    r2_train = compute_r2_score(y_train, y_train_pred)
    r2_test = compute_r2_score(y_test, y_test_pred)
    
    return r2_train, r2_test

# Initialize the models
linear_regression = LinearRegression()
ridge_regression = Ridge()
random_forest_regression = RandomForestRegressor(n_estimators=100, random_state=42)

# Train and evaluate the models
models = [linear_regression, ridge_regression, random_forest_regression]
model_names = ['Linear Regression', 'Ridge Regression', 'Random Forest Regression']
for i, model in enumerate(models):
    r2_train, r2_test = train_and_evaluate_model(model, X_train_scaled, y_train, X_test_scaled, y_test)
    print(f'{model_names[i]}: R^2 Score (Train) = {r2_train:.2f}, R^2 Score (Test) = {r2_test:.2f}')

# Feedforward Neural Network
class FeedforwardNeuralNetworkModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(FeedforwardNeuralNetworkModel, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim) 
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, output_dim)  

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

# Convert data to tensors
X_train_tensor = torch.tensor(X_train_scaled, dtype=torch.float)
y_train_tensor = torch.tensor(y_train.values, dtype=torch.float)
X_test_tensor = torch.tensor(X_test_scaled, dtype=torch.float)

# Define the model
input_dim = X_train_scaled.shape[1]
hidden_dim = 100
output_dim = 1
ffnn_model = FeedforwardNeuralNetworkModel(input_dim, hidden_dim, output_dim)

# Define loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.Adam(ffnn_model.parameters())

# Train the model
num_epochs = 100
for epoch in range(num_epochs):
    optimizer.zero_grad()
    outputs = ffnn_model(X_train_tensor)
    loss = criterion(outputs, y_train_tensor)
    loss.backward()
    optimizer.step()
    if (epoch+1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# Make predictions
y_train_pred = ffnn_model(X_train_tensor).detach().numpy()
y_test_pred = ffnn_model(X_test_tensor).detach().numpy()

# Compute R^2 score
r2_train = compute_r2_score(y_train, y_train_pred)
r2_test = compute
