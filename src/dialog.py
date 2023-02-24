
class Dialog:
    PREFIX = """
        You are now playing the role of the [sender], and your task is to reply to the [receiver] in the following dialogue. Your reply should not exceed 50 characters, and try to respond mainly in Chinese and English, and not all questions, occasionally you can tell a joke,
try not to repeat words
    """

    def generate_input(self, from_user_id, to_user_id, dialog):
        context = '\n'.join([str(d).replace(from_user_id, '[Sender]').replace(to_user_id, '[Receiver]') for d in dialog])
        return f'{self.PREFIX} \n\n{context}\n[Sender]:'
