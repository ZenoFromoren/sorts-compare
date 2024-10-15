import Sort
from test import build_plot, build_plot_repeating_elements, build_plot_partially_sorted


selection_sort = Sort.Selection_sort()
bubble_sort = Sort.Bubble_sort()
insertion_sort = Sort.Insertion_sort()
gnome_sort = Sort.Gnome_sort()

shell_sort = Sort.Shell_sort()
quick_sort = Sort.Quick_sort()
tree_sort = Sort.Tree_sort()

radix_lsd_sort = Sort.Radix_lsd_sort()
radix_msd_sort = Sort.Radix_msd_sort()
heap_sort = Sort.Heap_sort()
merge_recursive_sort = Sort.Merge_recursive_sort()
merge_iterative_sort = Sort.Merge_iterative_sort()

# power = 4

# build_plot(
#   power,
#   selection_sort,
#   bubble_sort,
#   insertion_sort,
#   gnome_sort
#   )

# build_plot(
#   power,
#   shell_sort,
#   quick_sort,
#   tree_sort,
#   )

# power = 5

# build_plot(
#   power,
#   radix_lsd_sort,
#   radix_msd_sort,
#   heap_sort,
#   merge_recursive_sort,
#   merge_iterative_sort
#   )


# power = 4

# build_plot_repeating_elements(
#   power,
#   selection_sort,
#   bubble_sort,
#   insertion_sort,
#   gnome_sort
#   )

# power = 3

# build_plot_repeating_elements(power,
#   shell_sort,
#   quick_sort,
#   tree_sort
#   )

# power = 7

# build_plot_repeating_elements(
#   power,
#   radix_lsd_sort,
#   radix_msd_sort,
#   heap_sort,
#   merge_recursive_sort,
#   merge_iterative_sort
#   )


power = 4

build_plot_partially_sorted(
  power,
  # selection_sort,
  # bubble_sort,
  insertion_sort,
  # gnome_sort
  )

# power = 3

# build_plot_partially_sorted(
#   power,
#   shell_sort,
#   quick_sort,
#   tree_sort
#   )

# power = 5

# build_plot_partially_sorted(
#   power,
#   radix_lsd_sort,
#   radix_msd_sort,
#   heap_sort,
#   merge_recursive_sort,
#   merge_iterative_sort
#   )
