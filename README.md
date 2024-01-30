SaaSafras Revenue Model README
Overview
This document outlines the revenue model implemented for SaaSafras, a plant care software company, focusing on strategic team allocation across New Business Acquisition, Account Management, and Support to maximize cumulative revenue over a 24-month period. The model is based on Python simulations that evaluate different allocation strategies to optimize revenue growth and customer base expansion.

Model Description
The revenue model simulates the impact of different team allocations on SaaSafras' revenue and customer retention. It incorporates key business metrics such as customer acquisition rates, churn rates, and the effect of customer satisfaction (CSAT) improvements on churn. The model explores five different scenarios, each with a unique allocation of resources to New Business Acquisition, Account Management, and Support.

Key Metrics
Initial Customer Base: 1,000 customers
Organic Growth Rate: 25 new customers/month
Baseline Churn Rate: 10%
Revenue per Customer: $100/month
CSAT Improvement Impact: Each support team member reduces churn by making customers more satisfied, directly influencing the churn rate.
New Business Acquisition: Each team member can acquire 5 new customers per month.
Account Management Capacity: Each manager can handle 25 customers, increasing their revenue by 20% month-over-month for up to 6 months.
Installation
To run the simulation model, ensure you have Python installed on your system. The model requires numpy and pandas libraries for execution. You can install these dependencies using pip: pip install numpy pandas

Usage
Clone the repository to your local machine.
Navigate to the directory containing the model.
Run the model using Python: python saasafras_revenue_model.py

The model will output the results for each simulation, including cumulative revenue, ending customer base, churn rate, and the number of managed accounts.
Scenario Summaries
Sim 1: Balanced focus on revenue growth.
Sim 2: Focused on new business acquisition.
Sim 3: Prioritized customer retention through support.
Sim 4: A balanced approach with a slight lean towards retention.
Sim 5: Eliminated account management in favor of support and new business acquisition, yielding the highest revenue.

Conclusion
The simulations revealed that prioritizing support and new business acquisition, especially eliminating account management roles, significantly boosts cumulative revenue and customer base growth.
