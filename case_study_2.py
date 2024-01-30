import numpy as np
import pandas as pd

# Initialize variables
months = 24
initial_customers = 1000
organic_growth = 25
baseline_churn = 0.10  # Initial churn rate
baseline_revenue_per_customer = 100  # Baseline monthly revenue per customer
team_size = 20  # Total size of the team
support_team_size = 11  # Number of team members in support
new_business_team_size = 9  # Number of team members in new business acquisition
account_management_team_size = team_size - support_team_size - new_business_team_size  # Number in account management
new_customers_per_team_member = 5  # New customers brought in by each new business team member
account_manager_capacity = 25  # Number of customers each account manager can handle
max_customers_under_management = account_management_team_size * account_manager_capacity  # Maximum customers under management

# Arrays to store monthly data
customer_base = np.zeros(months + 1, dtype=int)
revenue = np.zeros(months + 1)
churn_rate = np.full(months + 1, baseline_churn)

# Set initial values for month 0
customer_base[0] = initial_customers
revenue[0] = initial_customers * baseline_revenue_per_customer

# Simulation loop for each month
for month in range(1, months + 1):
    # Adjust churn rate based on CSAT improvement from the support team
    csat_improvement_points = support_team_size
    churn_rate[month] = baseline_churn * (0.85 ** csat_improvement_points)
    
    # Calculate the number of churned and new customers
    churned_customers = int(customer_base[month - 1] * churn_rate[month])
    new_customers = organic_growth + new_business_team_size * new_customers_per_team_member
    
    # Update customer base
    customer_base[month] = customer_base[month - 1] - churned_customers + new_customers
    
    # Calculate revenue from managed and non-managed customers
    managed_customers = min(customer_base[month], max_customers_under_management)
    non_managed_customers = customer_base[month] - managed_customers
    revenue_from_managed = managed_customers * baseline_revenue_per_customer * (1 + 0.20)**min(month, 6)
    revenue_from_non_managed = non_managed_customers * baseline_revenue_per_customer
    revenue[month] = revenue_from_managed + revenue_from_non_managed

# Compile results into a DataFrame
results = pd.DataFrame({
    "Month": np.arange(1, months + 1),
    "Customer Base": customer_base[1:],
    "Revenue": revenue[1:],
    "Churn Rate": churn_rate[1:],
    "Managed Customers": managed_customers
})

total_revenue_over_24_months = np.sum(revenue[1:])

print(results)
print(total_revenue_over_24_months)
