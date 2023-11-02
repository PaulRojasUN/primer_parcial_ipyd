#include <math.h>
#include <stdio.h>
#include <omp.h>

double calc_area_2(double a, double b, int rectangles) {

    double delta_x = (b - a)/rectangles;

    int number_of_threads = 4;


    double stride = (b - a)/number_of_threads;

    double k;
    int thread_id;
    double start_stride, end_stride;

    double acc_area = 0;

#pragma omp parallel private(k, start_stride, end_stride) shared(acc_area) num_threads(number_of_threads)
{

        start_stride = omp_get_thread_num()*stride + delta_x;
        end_stride = start_stride + stride;

        k = start_stride;

        while (k <= end_stride) {
            #pragma omp atomic
            acc_area += delta_x*(pow(sin(k), 3) + pow(cos(k), 3));
            k += delta_x;
        }
    }

    return acc_area;
}