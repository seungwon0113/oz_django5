from django.test import TestCase

# Create your tests here.
class MyTest(TestCase):

    def test_simple(self)->None:
        """
        Given: 게시글이 주어졌을 때 ( 테스트에 필요한 재료준비)
        When: 그 게시글에 좋아요를 하면 ( 실제로 테스트 하고자 하는 대상을 호출)
        Then: 좋아요 수가 1 증가 ( when에서 수행한 결과가 예상한 바와 일치하는지 검증
                                Then 에서 AssertionError가 발생했다면 테스트 실패다
                                테스트 실행도중에(Then 에서도) 아무런 에러도 발생하지 않는다면 성공.)
        """
        # Given
        a = 1
        b = 3

        # When
        result = a+b

        # Then
        self.assertEqual(result, 4)
