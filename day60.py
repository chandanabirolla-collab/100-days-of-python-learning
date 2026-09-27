class Phone:
    def __init__(self, brightness):
        self._brightness = brightness

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, value):
        self._brightness = value


phone = Phone(50)

print(phone.brightness)   # Getter

phone.brightness = 80     # Setter

print(phone.brightness)   # Getter