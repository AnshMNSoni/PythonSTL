#include <iostream>
#include <stack>
#include <vector>
#include <chrono>
#include <string>
#include <algorithm>

void run_stack() {
    auto start = std::chrono::high_resolution_clock::now();
    std::stack<int> s;
    for (int i = 0; i < 1000000; ++i) {
        s.push(i);
    }
    for (int i = 0; i < 1000000; ++i) {
        s.pop();
    }
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> diff = end - start;
    std::cout << diff.count() << std::endl;
}

void run_sort() {
    std::vector<int> arr(10000);
    for (int i = 0; i < 10000; ++i) {
        arr[i] = 10000 - i;
    }
    
    auto start = std::chrono::high_resolution_clock::now();
    int n = arr.size();
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n - 1 - i; ++j) {
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
            }
        }
    }
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> diff = end - start;
    std::cout << diff.count() << std::endl;
}

void run_next_permutation() {
    auto start = std::chrono::high_resolution_clock::now();
    std::vector<int> arr = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    while (std::next_permutation(arr.begin(), arr.end())) {
        // do nothing
    }
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> diff = end - start;
    std::cout << diff.count() << std::endl;
    // Prevent compiler optimization by printing array element to stderr
    std::cerr << "next_permutation check: " << arr[0] << std::endl;
}

void run_nth_element() {
    std::vector<int> arr(50000);
    for (int i = 0; i < 50000; ++i) {
        arr[i] = 50000 - i;
    }
    auto start = std::chrono::high_resolution_clock::now();
    std::nth_element(arr.begin(), arr.begin() + 25000, arr.end());
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> diff = end - start;
    std::cout << diff.count() << std::endl;
    // Prevent compiler optimization by printing array element to stderr
    std::cerr << "nth_element check: " << arr[25000] << std::endl;
}

void run_partition() {
    std::vector<int> arr(100000);
    for (int i = 0; i < 100000; ++i) {
        arr[i] = i;
    }
    auto start = std::chrono::high_resolution_clock::now();
    std::partition(arr.begin(), arr.end(), [](int x) { return x % 2 == 0; });
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> diff = end - start;
    std::cout << diff.count() << std::endl;
    // Prevent compiler optimization by printing array element to stderr
    std::cerr << "partition check: " << arr[0] << std::endl;
}

void run_binary_search() {
    std::vector<int> arr(1000000);
    for (int i = 0; i < 1000000; ++i) {
        arr[i] = i * 2;
    }
    auto start = std::chrono::high_resolution_clock::now();
    long long sum_indices = 0;
    for (int q = 0; q < 5000; ++q) {
        int target = q * 3;
        auto it = std::lower_bound(arr.begin(), arr.end(), target);
        sum_indices += std::distance(arr.begin(), it);
    }
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> diff = end - start;
    std::cout << diff.count() << std::endl;
    // Prevent compiler optimization by printing sum of indices to stderr
    std::cerr << "binary_search check: " << sum_indices << std::endl;
}

int main(int argc, char* argv[]) {
    std::string mode = "stack";
    if (argc > 1) {
        mode = argv[1];
    }
    if (mode == "sort") {
        run_sort();
    } else if (mode == "next_permutation") {
        run_next_permutation();
    } else if (mode == "nth_element") {
        run_nth_element();
    } else if (mode == "partition") {
        run_partition();
    } else if (mode == "binary_search") {
        run_binary_search();
    } else {
        run_stack();
    }
    return 0;
}
