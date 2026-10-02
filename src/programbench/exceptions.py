class EvalStepError(Exception):
    def __init__(self, error_code: str, error_details: str = ""):
        super().__init__(f"{error_code}: {error_details}")
        self.error_code = error_code
        self.error_details = error_details
