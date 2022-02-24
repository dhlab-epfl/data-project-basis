from os import path

data_folder = "../../data"
figures_folder = "../../report/figures"

# STEP 0 download data
# ===================================

s0_folder = path.join(data_folder, "s0_downloaded_data")

s0_balzac_books = path.join(s0_folder, "balzac_books.json")

s0_figure_sinusoid = path.join(figures_folder, "s0_sinusoid.png")

# STEP 1 train model
# ===================================

# ...