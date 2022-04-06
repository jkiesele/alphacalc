#include <pybind11/pybind11.h>

#include "alpha_intersect.h"

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

namespace py = pybind11;

PYBIND11_MODULE(alphacalc, m) {
    m.doc() = "alphacalc_module";
    m.def("alpha", &alpha, "Calculates alpha");
    m.def("find_intersection", &find_intersection, "finds intersection point in t");

#ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif
}
