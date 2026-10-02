#We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.
#For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
#Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

class Solution(object):

    def asteroidCollision(self, asteroids):

        stack = []

        for asteroid in asteroids:

            # Collision can happen only when:
            # stack top is moving right (+)
            # current asteroid is moving left (-)
            while stack and stack[-1] > 0 and asteroid < 0:

                if stack[-1] < abs(asteroid):
                    # Top asteroid explodes
                    stack.pop()

                elif stack[-1] == abs(asteroid):
                    # Both explode
                    stack.pop()
                    asteroid = 0
                    break

                else:
                    # Current asteroid explodes
                    asteroid = 0
                    break

            if asteroid != 0:
                stack.append(asteroid)

        return stack