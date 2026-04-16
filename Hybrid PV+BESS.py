import matplotlib.dates as mdates

# Assuming this is part of your graph plotting code
# Set major locator and formatter for the x-axis
ax.xaxis.set_major_locator(mdates.HourLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

# Your existing code for plotting the graph goes here...