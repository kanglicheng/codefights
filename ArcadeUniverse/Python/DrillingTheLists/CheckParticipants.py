def checkParticipants(participants):
    return [k for k in range(len(participants)) if participants[k] < k]
