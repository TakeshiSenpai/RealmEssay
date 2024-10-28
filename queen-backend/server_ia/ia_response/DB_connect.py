import sys,pathlib,json
sys.path.append(str(pathlib.Path(__file__).parent.parent.parent.parent.resolve()))
from database.ChatDB import Chat

INTERACTIONS_FILE =pathlib.Path('queen-backend/server_ia/ia_response/interactions.json').resolve()


def test_post():
    Chat.post.crear_chat_desde_json()