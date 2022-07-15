def vocation_status_modifier(default_value, vocation, data):
    data["strength"] = default_value + int(vocation.strength_modifier)
    data["intellect"] = default_value + int(vocation.intellect_modifier)
    data["agility"] = default_value + int(vocation.agility_modifier)

    return data
