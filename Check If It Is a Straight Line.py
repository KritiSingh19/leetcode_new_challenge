"""You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane."""

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if (len(coordinates)==2):
            return True
        d=(coordinates[1][0]-coordinates[0][0])
        if(d==0):
            for i in range (2,len(coordinates)):
                c=(coordinates[i][0]-coordinates[0][0])
                if(c!=d):
                    return False
        else:
            a=(coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
            for i in range (2,len(coordinates)):  
                dy=coordinates[i][1]-coordinates[0][1]
                dx=coordinates[i][0]-coordinates[0][0]
                if(dx==0):
                    return False
                else:
                    b=dy/dx
                    if(a!=b):
                        return False
        return True
