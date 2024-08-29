from button import Button
class ButtonManager():
    def __init__(self, display, button_images, hover_button_images) -> None:
        self.display = display
        self.button_images = button_images
        self.hover_button_images = hover_button_images


    def render_buttons(self, mouse_pos):
        x_distance_between_buttons = 0

        for idx, (scaled_button_image, scaled_hover_button_image) in enumerate(zip(self.button_images, self.hover_button_images)):
            # 0, (rojo.png, rojo_hover.png)
            # 1, (verde.png, ...)

            # Create the Button Instance to draw on screen
            button = Button(color_number=idx)
            button_pos_x = x_distance_between_buttons + button.grid_start_x
            button_pos_y = button.button_pos_y
            
            if button.x_scale + button.grid_start_x + x_distance_between_buttons > mouse_pos[0] > button.grid_start_x + x_distance_between_buttons \
            and button.y_scale + button.button_pos_y + button.y_margin > mouse_pos[1] > button.button_pos_y + button.y_margin:
        
                button.draw_bright_button(display=self.display,
                                            scaled_image=scaled_hover_button_image, 
                                            pos_x=button_pos_x, 
                                            pos_y=button_pos_y)

            else:    
                button.draw_button(display=self.display,
                                        scaled_image=scaled_button_image,
                                        pos_x=button_pos_x,
                                        pos_y=button_pos_y)

            # update the distance between buttons
            x_distance_between_buttons += button.x_scale + 10


    def handle_color_change(self, mouse_pos):
        x_distance_between_buttons = 0
        for idx, (scaled_button_image, scaled_hover_button_image) in enumerate(zip(self.button_images, self.hover_button_images)):
            # 0, (rojo.png, rojo_hover.png)
            # 1, (verde.png, ...)

            # Create the Button Instance to draw on screen
            button = Button(color_number=idx)
            
            if button.x_scale + button.grid_start_x + x_distance_between_buttons > mouse_pos[0] > button.grid_start_x + x_distance_between_buttons \
            and button.y_scale + button.button_pos_y + button.y_margin > mouse_pos[1] > button.button_pos_y + button.y_margin:
                self.current_color = button.color_number
                print(f"changing current color to {self.current_color}")

            x_distance_between_buttons += button.x_scale + 10

        return self.current_color