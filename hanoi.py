def hanoi(disks, source, auxiliary, target):
    if disks == 1:
        print('Move disk 1 from block {} to block {}.'.format(source, target))
        return
 
    hanoi(disks - 1, source, target, auxiliary)
    print('Move disk {} from block {} to block {}.'.format(disks, source, target))
    hanoi(disks - 1, auxiliary, source, target)
 
 
disks = int(input('Enter number of disks: '))
hanoi(disks, 'A', 'B', 'C')