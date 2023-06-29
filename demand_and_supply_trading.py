import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def demand_and_supply(price, demand, supply):
  """
  Calculates the demand and supply zones for a given price.

  Args:
    price: The price of the asset.
    demand: The demand curve.
    supply: The supply curve.

  Returns:
    A DataFrame with the demand and supply zones.
  """

  zones = pd.DataFrame({
    "Demand Zone": price <= demand,
    "Supply Zone": price >= supply
  })

  return zones

def find_entry_point(price, demand, supply):
  """
  Finds the entry point for a trade based on the demand and supply zones.

  Args:
    price: The price of the asset.
    demand: The demand curve.
    supply: The supply curve.

  Returns:
    The price at which to enter the trade.
  """

  zones = demand_and_supply(price, demand, supply)

  # If the price is in the demand zone, recommend buying.

  if zones["Demand Zone"].any():
    return price[zones["Demand Zone"].idxmax()]

  # If the price is in the supply zone, recommend selling.

  elif zones["Supply Zone"].any():
    return price[zones["Supply Zone"].idxmin()]

  # Otherwise, don't recommend entering a trade.

  else:
    return None

def main():
  # Get the price data.
  price = np.linspace(0, 100, 100)

  # Get the demand curve.
  demand = 100 - price

  # Get the supply curve.
  supply = price

  # Find the entry point for a trade.
  entry_point = find_entry_point(price, demand, supply)

  # Print the entry point.
  print(entry_point)

if __name__ == "__main__":
  main()

demand_curve = np.array([100, 90, 80, 70, 60, 50, 40, 30, 20, 10])
supply_curve = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

plt.plot(demand_curve, label='Demand')
plt.plot(supply_curve, label='Supply')
plt.xlabel('Price')
plt.ylabel('Quantity')
plt.legend()
plt.show()

potential_opportunities = np.where(demand_curve > supply_curve)[0]
print("Potential trading opportunities at prices:", potential_opportunities)

# Find the equilibrium price index
equilibrium_index = np.where(demand_curve == supply_curve)[0]

if equilibrium_index.size > 0:
    equilibrium_price = demand_curve[equilibrium_index]
    print("Equilibrium price:", equilibrium_price)
else:
    print("No equilibrium price found.")

