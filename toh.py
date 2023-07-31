def tower_of_hanoi(n, source, destination, spare):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    tower_of_hanoi(n - 1, source, spare, destination)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, spare, destination, source)

# Example usage:
num_disks = 3  # Replace this with the number of disks you want to solve for
tower_of_hanoi(num_disks, 'A', 'C', 'B')
