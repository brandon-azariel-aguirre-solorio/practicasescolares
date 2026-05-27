def hanoi_solver(n):
    source = list(range(n, 0, -1))
    auxiliary = []
    target = []

    moves = []
    moves.append(f"{source} {auxiliary} {target}")

    def solve(num_disks, src, aux, dst):
        if num_disks == 1:
            dst.append(src.pop())
            moves.append(f"{source} {auxiliary} {target}")
            return

        solve(num_disks - 1, src, dst, aux)

        dst.append(src.pop())
        moves.append(f"{source} {auxiliary} {target}")

        solve(num_disks - 1, aux, src, dst)

    solve(n, source, auxiliary, target)

    return "\n".join(moves)

print(hanoi_solver(10))
