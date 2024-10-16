from tabom.models import Like


def do_like(user_id: int, article_id: int) -> Like:
    # # 좋아요 생성 전
    # try:
    #     # 좋아요가 있는지 SELECT
    #     like = Like.objects.filter(user_id=user_id, article_id=article_id).get()
    #     # 좋아요가 이미 있으면 raise Exception
    #     raise Exception
    # except Like.DoesNotExist:
    #     pass

    if Like.objects.filter(user_id=user_id, article_id=article_id).exists():
        raise Exception

    return Like.objects.create(user_id=user_id, article_id=article_id)
