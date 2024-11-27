def generate_url(rank, role):
    ranks_url_map = {
        "Herald": "herald", "Guardian": "guardian", "Crusader": "crusader",
        "Archon": "archon", "Legend": "legend", "Ancient": "ancient",
        "Divine": "divine", "Immortal": "immortal"
    }
    roles_url_map = {
        "Carry": "core-safe", "Mid": "core-mid", "Offlaner": "core-off",
        "Soft Support": "support-safe", "Hard Support": "support-off"
    }
    base_url = "https://uk.dotabuff.com/heroes?show=facets&view=meta&mode=all-pick&date=7d&rankTier={rank}&position={position}"
    rank_param = ranks_url_map.get(rank, "herald")
    role_param = roles_url_map.get(role, "core-safe")
    return base_url.format(rank=rank_param, position=role_param)