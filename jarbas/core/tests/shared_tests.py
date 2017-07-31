from django.test import TestCase

# Serializer methods: TestSerializer


def test_serializer(TestCase, obj, expected, input):
    serialized = obj.serialize(input)
    TestCase.assertEqual(serialized, expected)


# Cotum methods:  TestCustomMethods


def test_main(TestCase, obj, update, schedule_update, costum_method):
    costum_method.return_value = (range(21), range(21, 43))
    obj.main()
    update.assert_has_calls([call()] * 2)
    schedule_update.assert_has_calls(call(i) for i in range(42))
