from os.path import join as j

relative_path_to_root = j("..","..")

# use and abuse from os.path.join() (here aliased as "j") it ensures cross OS compatible paths
data_folder = j(relative_path_to_root, "data")
figures_folder = j(relative_path_to_root, "report", "figures")

# STEP 0 download data
# ===================================

s0_folder = j(data_folder, "s0_downloaded_data")

s0_balzac_books = j(s0_folder, "balzac_books.json")

s0_figure_sinusoid = j(figures_folder, "s0_sinusoid.png")

# STEP 1 train model
# ===================================

# ...