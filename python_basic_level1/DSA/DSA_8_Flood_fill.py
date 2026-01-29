class Solution(object):
    def floodFill(self, image, sr, sc, color):
        val = image[sr][sc]

        # important base case
        if val == color:
            return image

        def logic(row, col):
            if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]):
                return

            if image[row][col] != val:
                return

            image[row][col] = color

            logic(row + 1, col)
            logic(row - 1, col)
            logic(row, col + 1)
            logic(row, col - 1)

        logic(sr, sc)
        return image
