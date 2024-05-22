from backend.MemberInfo import MemberInfo

class User:
    """Class that stores user information about session and user's chat"""
    
    auth_state: bool
    member_info: MemberInfo
    
    team: str
    team_id: int
    sheets__team_row: int
    
    teammates: list

    
    def __init__(self, team: str = "", team_id: int = 0, sheets__team_row: int = 0, teammates: list = [], member_info: MemberInfo = MemberInfo(), auth_state: bool = False) -> None:
        """Initializes the user object with chat_id and auth_state (False by default)"""
        self.auth_state = auth_state
        self.member_info = member_info

        self.team = team
        self.team_id = team_id
        self.sheets__team_row = sheets__team_row

        self.teammates = teammates
        
    def __str__(self):
        """Debug output for User"""
        # return f"User auth_state: {self.auth_state}, team: {self.team} member_info: {self.member_info}"

        answer: str = f"User(auth_state: {self.auth_state} | team: {self.team} | team_id: {self.team_id} | sheets__team_row: {self.sheets__team_row} | member_info: {self.member_info})"
        return answer


    def __eq__(self, other) -> bool:
        """Compares two User objects"""
        if (self.member_info == other.member_info):
            return True
        return False
    
    
    def count_teammates(self) -> int:
        """Returns the number of teammates in the list of teammates"""
        
        return len(self.teammates)
    
    def print_teammates(self) -> str:
        """Prints out all teammates in the profile"""

        if self.count_teammates() == 0:
            return "No teammates yet"
        print(f"Teammates:")
        for teammate in self.teammates:
            print(f"  {teammate}")