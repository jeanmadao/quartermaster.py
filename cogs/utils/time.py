def calulate_delta_seconds(epoch_a, epoch_b):
    return abs(epoch_a - epoch_b)

def calculate_delta_minutes(epoch_a, epoch_b):
    return abs(epoch_a - epoch_b) / 60

def calculate_delta_hours(epoch_a, epoch_b):
    return abs(epoch_a - epoch_b) / 3600
