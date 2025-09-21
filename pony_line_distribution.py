import csv

Twilight_Sparkle = 4381
Rarity = 2433
Pinkie_Pie = 2690
Rainbow_Dash = 2848
Fluttershy = 2045
Total_lines = 36860

Twilight_Sparkle_percentage = f"{(Twilight_Sparkle / Total_lines) * 100:.2f}%"
Rarity_percentage = f"{(Rarity / Total_lines) * 100:.2f}%"
Pinkie_Pie_percentage = f"{(Pinkie_Pie / Total_lines) * 100:.2f}%"
Rainbow_Dash_percentage = f"{(Rainbow_Dash / Total_lines) * 100:.2f}%"
Fluttershy_percentage = f"{(Fluttershy / Total_lines) * 100:.2f}%"

rows = [
    ["pony_name", "total_line_count", "percent_all_lines"],
    ["Twilight Sparkle", Twilight_Sparkle, Twilight_Sparkle_percentage],
    ["Rarity", Rarity, Rarity_percentage],
    ["Pinkie Pie", Pinkie_Pie, Pinkie_Pie_percentage],
    ["Rainbow Dash", Rainbow_Dash, Rainbow_Dash_percentage],
    ["Fluttershy", Fluttershy, Fluttershy_percentage]
]

with open("line_percentages.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)
