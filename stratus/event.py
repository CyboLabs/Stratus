class ChatEvent:
    """
    Represents a single event happening in an IRC conversation.
    Examples include nick changing, a message, channel joins, etc.
    """
    def __init__(self, message):
        pass


class HookEvent:
    """
    Represents a plugin hook fired from an Event.
    """
    def __init__(self, parent):
        """

        Args:
            parent (ChatEvent): The ChatEvent that triggered this HookEvent.

        Returns:

        """
