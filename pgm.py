class Pgm:
    def __init__(self):
        self.Pixels = []

    def read(self, file: str) -> bool:
        try:
            with open(file, 'r') as fin:
                s = fin.readline().strip()
                if s != 'P2':
                    return False

                dimensions = fin.readline().strip().split()
                if len(dimensions) != 2:
                    return False
                c, r = map(int, dimensions)
                if c <= 0 or r <= 0:
                    return False

                max_val = int(fin.readline().strip())
                if max_val != 255:
                    return False

                self.Pixels = []
                for _ in range(r):
                    line = fin.readline()
                    # Handle cases where multiple spaces or line breaks separate pixels
                    row = []
                    for value in line.strip().split():
                        if not value.isdigit():
                            return False
                        v = int(value)
                        if v > 255:
                            return False
                        row.append(v)
                    if len(row) != c:
                        return False
                    self.Pixels.append(row)

                # Check for extra content after pixels
                remaining = fin.read().strip()
                if remaining:
                    return False
            return True
        except:
            return False

    def write(self, file: str) -> bool:
        try:
            if not self.Pixels or not self.Pixels[0]:
                return False

            with open(file, 'w') as fout:
                fout.write("P2\n")
                fout.write(f"{len(self.Pixels[0])} {len(self.Pixels)}\n")
                fout.write("255\n")

                count = 0
                total_pixels = sum(len(row) for row in self.Pixels)

                for row in self.Pixels:
                    for pixel in row:
                        fout.write(f"{pixel}")
                        count += 1
                        if count % 20 == 0:
                            fout.write("\n")
                        elif count < total_pixels:
                            fout.write(" ")

                if count % 20 != 0:
                    fout.write("\n")
            return True
        except:
            return False

    def create(self, r: int, c: int, pv: int) -> bool:
        if r == 0 or c == 0 or pv > 255:
            return False
        self.Pixels = [[pv] * c for _ in range(r)]
        return True

    def clockwise(self) -> bool:
        if not self.Pixels:
            return False
        r = len(self.Pixels)
        c = len(self.Pixels[0])
        # Rotate 90 degrees clockwise
        self.Pixels = [[self.Pixels[r - i - 1][j] for i in range(r)] for j in range(c)]
        return True

    def counterclockwise(self) -> bool:
        if not self.Pixels:
            return False
        r = len(self.Pixels)
        c = len(self.Pixels[0])
        # Rotate 90 degrees counterclockwise
        self.Pixels = [[self.Pixels[i][c - j - 1] for i in range(r)] for j in range(c)]
        return True

    def pad(self, w: int, pv: int) -> bool:
        if w == 0 or pv > 255:
            return False
        if not self.Pixels:
            return False
        r, c = len(self.Pixels), len(self.Pixels[0])
        # Create padded pixels with value pv
        pad = [[pv] * (c + 2 * w) for _ in range(r + 2 * w)]
        for i in range(r):
            for j in range(c):
                pad[i + w][j + w] = self.Pixels[i][j]
        self.Pixels = pad
        return True

    def panel(self, r: int, c: int) -> bool:
        if r == 0 or c == 0:
            return False
        if not self.Pixels:
            return False
        row, col = len(self.Pixels), len(self.Pixels[0])
        # Create paneled pixels
        panel = [[0] * (c * col) for _ in range(r * row)]

        for i in range(r):
            for j in range(c):
                for x in range(row):
                    for y in range(col):
                        panel[i * row + x][j * col + y] = self.Pixels[x][y]

        self.Pixels = panel
        return True

    def crop(self, r: int, c: int, rows: int, cols: int) -> bool:
        try:
            if r + rows > len(self.Pixels) or c + cols > len(self.Pixels[0]):
                return False
            crop = [[self.Pixels[r + i][c + j] for j in range(cols)] for i in range(rows)]
            self.Pixels = crop
            return True
        except IndexError:
            return False
