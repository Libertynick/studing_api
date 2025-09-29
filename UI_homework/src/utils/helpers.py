MAX_BODY_SIZE = 150  # Максимальный размер тела в байтах

def truncate_body(body: str, max_size: int = MAX_BODY_SIZE) -> str:
    if len(body.encode("utf-8")) > max_size:
        body = "<TRUNCATED> " + body.encode("utf-8")[:max_size].decode("utf-8", "ignore")
    return body