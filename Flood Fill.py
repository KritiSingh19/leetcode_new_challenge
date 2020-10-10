An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image





class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColour: int) -> List[List[int]]:
        rows , cols = len(image) , len(image[0])
        directions = [(1 , 0) , (-1 , 0) , (0 , 1) , (0 , -1)]
        def fillColor(x , y , old_color):
            if image[x][y] != old_color:
                return 
            if image[x][y] == newColour:
                return
            image[x][y] = newColour
            for dx , dy in directions:
                nx , ny = x + dx , y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    fillColor(nx , ny , old_color)
        fillColor(sr , sc , image[sr][sc])
        return image
		






