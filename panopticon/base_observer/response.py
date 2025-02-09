class ObserverResponse:
    def __init__(self, status: bool, data: any = None, message: str = None):
        self.status = status
        self.data = data
        self.message = message

    def to_dict(self):
        return {
            "status": str(self.status),
            "data": str(self.data),
            "message": str(self.message),
        }

    def __dir__(self):
        return ["status", "data", "message"]

    def __str__(self):
        return str(self.to_dict())