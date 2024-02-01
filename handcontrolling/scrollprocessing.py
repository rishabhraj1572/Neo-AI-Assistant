import math
import mouse

Active = True
Inactive = False

def distance(p1, p2):
    xdiff = p1.x - p2.x
    ydiff = p1.y - p2.y
    return math.sqrt((xdiff ** 2) + (ydiff ** 2))

def scroll_change(hand_coordinates, previous_scrollwheel):
    fingertip = hand_coordinates.landmark[16]
    fingerstart = hand_coordinates.landmark[13]
    wrist = hand_coordinates.landmark[0]

    if distance(fingertip, wrist) < distance(fingerstart, wrist):
        scrollwheel = Active
    else:
        scrollwheel = Inactive

    if not scrollwheel and not previous_scrollwheel:
        # print("scrollwheel inactive")
        return scrollwheel, False
    elif scrollwheel and not previous_scrollwheel:
        # print("scrollwheel becoming active.......")
        return scrollwheel, True
    elif not scrollwheel and previous_scrollwheel:
        # print('Scrollwheel deactivating......')
        return scrollwheel, True
    else:
        # print("Scrollwheel active")
        return scrollwheel, False

def scrolling(hand_coordinates, previous_hand_coordinates, is_scrollwheel_active, scrollwheel_state_change, previous_mouse_position):
    if not is_scrollwheel_active and not scrollwheel_state_change:
        return
    elif is_scrollwheel_active and scrollwheel_state_change:
        mouse.click(button='middle')
    elif not is_scrollwheel_active and scrollwheel_state_change:
        mouse.click(button='left')
    else:
        mouse_x = previous_mouse_position[0] / 1535
        mouse_y = previous_mouse_position[1] / 863
        finger_x = previous_hand_coordinates.landmark[8].x - hand_coordinates.landmark[8].x
        finger_y = previous_hand_coordinates.landmark[8].y - hand_coordinates.landmark[8].y
        relative_x = (finger_x + mouse_x) * 1535
        relative_y = (finger_y + mouse_y) * 863
        mouse.move(relative_x, relative_y)

# 1535 863