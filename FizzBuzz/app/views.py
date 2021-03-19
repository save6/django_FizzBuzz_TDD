from django.shortcuts import render
from django.views.generic import TemplateView

class FizzBuzzView(TemplateView):
    
    def convert(self, num):
        if(num % 3 == 0 and num % 5 == 0):
            return "FizzBuzz"

        elif(num % 3 == 0):
            return "Fizz"

        elif(num % 5 == 0):
            return "Buzz"

        return str(num)
    
    def get(self, request):
        NUM_LIST = "1 2 3 4 5 6 7 8 9 \n\
 10 11 12 13 14 15 16 17 18 19 \n\
 20 21 22 23 24 25 26 27 28 29 \n\
 30 31 32 33 34 35 36 37 38 39 \n\
 40 41 42 43 44 45 46 47 48 49 \n\
 50 51 52 53 54 55 56 57 58 59 \n\
 60 61 62 63 64 65 66 67 68 69 \n\
 70 71 72 73 74 75 76 77 78 79 \n\
 80 81 82 83 84 85 86 87 88 89 \n\
 90 91 92 93 94 95 96 97 98 99 \n\
 100"
        return render(request, 'app/FizzBuzz.html', {'num_list':NUM_LIST})

    def post(self, request):
        num_list = request.POST['num_list']
        result_list = num_list.split(' ')

        for i, num in enumerate(result_list):
            if num.isdecimal() :
                result_list[i] = self.convert(int(num))
            else :
                if num != '\n' and num != '\r\n':
                    result_list[i] = "NotNum"

        result = ' '.join(result_list)

        return render(request, 'app/FizzBuzz.html', {'num_list':result})
