import numpy as np
import matplotlib.pyplot as plt


def draw(categories: list[str], values: list[int]) -> None:
    ax = None
    num_categories: int = len(categories)
    # Compute angle for each axis
    angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()

    values.append(values[0])
    angles.append(angles[0])

    # Plot
    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='skyblue', alpha=0.4)
    ax.plot(angles, values, color='blue', linewidth=2, linestyle='solid')
    
    # Set the labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=10, rotation=45)
    ax.yaxis.grid(True)
    # ax.tick_params(axis='x', pad=30)  # Adjust the offset here

    ax.set_yticks(range(0, 11))
    plt.show()

# ! TEST
categories = ['Производительность', 'Надежность', 'Инновации', 'Поддержка', 'Цена']
values = [4, 3, 4.5, 3.5, 2.5]


draw(categories, values)
