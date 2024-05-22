class MemberInfo:
    """
    Class that stores profile details, teammates info
    and information gathered from database 
    """

    full_name: str
    sheets__member_row: int
    
    
    def __init__(self, full_name: str = "", sheets__member_row: int = 0) -> None:
        """
        Initializes the MemberInfo object with full_name (empty by default)
        and row_number (0 by default)
        """
        
        self.full_name = full_name
        self.sheets__member_row = sheets__member_row
        
    def __str__(self) -> str:
        """Debug output for MemberInfo"""
        
        answer: str = f"MemberInfo(full_name: {self.full_name} | sheets__member_row: {self.sheets__member_row})"
        return answer

    def __eq__(self, value: object) -> bool:
        """Compares two Profile objects"""
        
        if (self.full_name == value.full_name and self.sheets__member_row == value.sheets__member_row):
            return True
        return False