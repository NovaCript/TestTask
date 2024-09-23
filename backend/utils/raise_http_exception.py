from fastapi import HTTPException, status


class RaiseHttpException:
    @staticmethod
    def invalid_date_format():
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid date format",
        )

    @staticmethod
    def walk_duration_too_long():
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Прогулка может длиться не более получаса",
        )

    @staticmethod
    def walk_too_early():
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Самая ранняя прогулка может начинаться не ранее 7-ми утра",
        )

    @staticmethod
    def walk_too_late():
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Самая поздняя прогулка может начинаться не позднее 11-ти вечера",
        )

    @staticmethod
    def already_walking():
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Пётр и Антон каждый могут гулять одновременно только с одним животным",
        )


ex = RaiseHttpException()
