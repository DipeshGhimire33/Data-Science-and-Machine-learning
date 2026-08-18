class PassCheck:
    """Check the basic strength of a password."""

    def __init__(self, password: str):
        """Initialize the password."""
        self.password = password

    def check(self) -> str:
        """Return whether the password is strong or weak."""
        if (
            len(self.password) >= 8
            and not self.password.isalpha()
            and not self.password.isdigit()
        ):
            return "Strong password"

        return "Weak password"


password_checker = PassCheck("hello12345")

print(password_checker.check())
             