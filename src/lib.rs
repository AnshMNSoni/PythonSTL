use pyo3::prelude::*;
use pyo3::types::PyList;
use std::collections::{VecDeque, BTreeSet, BTreeMap};
use std::cmp::Ordering;

// ----------------- PyObjectOrd Bridge -----------------

/// A wrapper for PyObject to enable sorted indexing inside Rust's BTreeSet/BTreeMap.
/// It delegates Eq, Ord, PartialEq, and PartialOrd to Python rich comparisons.
#[derive(Clone)]
struct PyObjectOrd(PyObject);

impl PartialEq for PyObjectOrd {
    fn eq(&self, other: &Self) -> bool {
        Python::with_gil(|py| {
            let self_ref = self.0.bind(py);
            let other_ref = other.0.bind(py);
            if let (Ok(a), Ok(b)) = (self_ref.extract::<i64>(), other_ref.extract::<i64>()) {
                return a == b;
            }
            if let (Ok(a), Ok(b)) = (self_ref.extract::<f64>(), other_ref.extract::<f64>()) {
                return a == b;
            }
            if let (Ok(a), Ok(b)) = (self_ref.extract::<&str>(), other_ref.extract::<&str>()) {
                return a == b;
            }
            self_ref.eq(other_ref).unwrap_or(false)
        })
    }
}

impl Eq for PyObjectOrd {}

impl PartialOrd for PyObjectOrd {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for PyObjectOrd {
    fn cmp(&self, other: &Self) -> Ordering {
        Python::with_gil(|py| {
            let self_ref = self.0.bind(py);
            let other_ref = other.0.bind(py);
            if let (Ok(a), Ok(b)) = (self_ref.extract::<i64>(), other_ref.extract::<i64>()) {
                return a.cmp(&b);
            }
            if let (Ok(a), Ok(b)) = (self_ref.extract::<f64>(), other_ref.extract::<f64>()) {
                if let Some(ord) = a.partial_cmp(&b) {
                    return ord;
                }
            }
            if let (Ok(a), Ok(b)) = (self_ref.extract::<&str>(), other_ref.extract::<&str>()) {
                return a.cmp(&b);
            }
            if self_ref.eq(other_ref).unwrap_or(false) {
                Ordering::Equal
            } else if self_ref.lt(other_ref).unwrap_or(false) {
                Ordering::Less
            } else {
                Ordering::Greater
            }
        })
    }
}

// ----------------- RustStack -----------------

#[pyclass]
struct RustStack {
    data: Vec<PyObject>,
}

#[pymethods]
impl RustStack {
    #[new]
    fn new() -> Self {
        RustStack { data: Vec::new() }
    }

    fn push(&mut self, value: PyObject) {
        self.data.push(value);
    }

    fn pop(&mut self) -> PyResult<()> {
        if !self.data.is_empty() {
            self.data.pop();
        }
        Ok(())
    }

    fn top(&self, py: Python) -> PyResult<Option<PyObject>> {
        if self.data.is_empty() {
            Ok(None)
        } else {
            Ok(Some(self.data.last().unwrap().clone_ref(py)))
        }
    }

    fn empty(&self) -> bool {
        self.data.is_empty()
    }

    fn size(&self) -> usize {
        self.data.len()
    }

    fn get_data(&self, py: Python) -> PyResult<Vec<PyObject>> {
        Ok(self.data.iter().map(|x| x.clone_ref(py)).collect())
    }

    fn set_data(&mut self, new_data: Vec<PyObject>) {
        self.data = new_data;
    }
}

// ----------------- RustQueue -----------------

#[pyclass]
struct RustQueue {
    data: VecDeque<PyObject>,
}

#[pymethods]
impl RustQueue {
    #[new]
    fn new() -> Self {
        RustQueue { data: VecDeque::new() }
    }

    fn push(&mut self, value: PyObject) {
        self.data.push_back(value);
    }

    fn pop(&mut self) -> PyResult<()> {
        if !self.data.is_empty() {
            self.data.pop_front();
        }
        Ok(())
    }

    fn front(&self, py: Python) -> PyResult<Option<PyObject>> {
        if self.data.is_empty() {
            Ok(None)
        } else {
            Ok(Some(self.data.front().unwrap().clone_ref(py)))
        }
    }

    fn back(&self, py: Python) -> PyResult<Option<PyObject>> {
        if self.data.is_empty() {
            Ok(None)
        } else {
            Ok(Some(self.data.back().unwrap().clone_ref(py)))
        }
    }

    fn empty(&self) -> bool {
        self.data.is_empty()
    }

    fn size(&self) -> usize {
        self.data.len()
    }

    fn get_data(&self, py: Python) -> PyResult<Vec<PyObject>> {
        Ok(self.data.iter().map(|x| x.clone_ref(py)).collect())
    }

    fn set_data(&mut self, new_data: Vec<PyObject>) {
        self.data = new_data.into();
    }
}

// ----------------- RustVector -----------------

#[pyclass]
struct RustVector {
    data: Vec<PyObject>,
}

#[pymethods]
impl RustVector {
    #[new]
    fn new() -> Self {
        RustVector { data: Vec::new() }
    }

    fn push_back(&mut self, value: PyObject) {
        self.data.push(value);
    }

    fn pop_back(&mut self) -> PyResult<()> {
        if !self.data.is_empty() {
            self.data.pop();
        }
        Ok(())
    }

    fn at(&self, index: usize, py: Python) -> PyResult<Option<PyObject>> {
        if index >= self.data.len() {
            Ok(None)
        } else {
            Ok(Some(self.data[index].clone_ref(py)))
        }
    }

    fn insert(&mut self, index: usize, value: PyObject) -> PyResult<()> {
        if index <= self.data.len() {
            self.data.insert(index, value);
        }
        Ok(())
    }

    fn erase(&mut self, index: usize) -> PyResult<()> {
        if index < self.data.len() {
            self.data.remove(index);
        }
        Ok(())
    }

    fn clear(&mut self) {
        self.data.clear();
    }

    fn reserve(&mut self, capacity: usize) {
        self.data.reserve(capacity);
    }

    fn shrink_to_fit(&mut self) {
        self.data.shrink_to_fit();
    }

    fn size(&self) -> usize {
        self.data.len()
    }

    fn capacity(&self) -> usize {
        self.data.capacity()
    }

    fn empty(&self) -> bool {
        self.data.is_empty()
    }

    fn get_data(&self, py: Python) -> PyResult<Vec<PyObject>> {
        Ok(self.data.iter().map(|x| x.clone_ref(py)).collect())
    }

    fn set_data(&mut self, new_data: Vec<PyObject>) {
        self.data = new_data;
    }
}

// ----------------- RustSet -----------------

#[pyclass]
struct RustSet {
    data: BTreeSet<PyObjectOrd>,
}

#[pymethods]
impl RustSet {
    #[new]
    fn new() -> Self {
        RustSet { data: BTreeSet::new() }
    }

    fn insert(&mut self, value: PyObject) -> bool {
        self.data.insert(PyObjectOrd(value))
    }

    fn erase(&mut self, value: PyObject) -> bool {
        self.data.remove(&PyObjectOrd(value))
    }

    fn find(&self, value: PyObject) -> bool {
        self.data.contains(&PyObjectOrd(value))
    }

    fn empty(&self) -> bool {
        self.data.is_empty()
    }

    fn size(&self) -> usize {
        self.data.len()
    }

    fn get_data(&self, py: Python) -> PyResult<Vec<PyObject>> {
        Ok(self.data.iter().map(|x| x.0.clone_ref(py)).collect())
    }

    fn set_data(&mut self, new_data: Vec<PyObject>) {
        self.data = new_data.into_iter().map(PyObjectOrd).collect();
    }
}

// ----------------- RustMap -----------------

#[pyclass]
struct RustMap {
    data: BTreeMap<PyObjectOrd, PyObject>,
}

#[pymethods]
impl RustMap {
    #[new]
    fn new() -> Self {
        RustMap { data: BTreeMap::new() }
    }

    fn insert(&mut self, key: PyObject, value: PyObject) {
        self.data.insert(PyObjectOrd(key), value);
    }

    fn erase(&mut self, key: PyObject) -> bool {
        self.data.remove(&PyObjectOrd(key)).is_some()
    }

    fn find(&self, key: PyObject) -> bool {
        self.data.contains_key(&PyObjectOrd(key))
    }

    fn at(&self, key: PyObject, py: Python) -> PyResult<Option<PyObject>> {
        if let Some(val) = self.data.get(&PyObjectOrd(key)) {
            Ok(Some(val.clone_ref(py)))
        } else {
            Ok(None)
        }
    }

    fn empty(&self) -> bool {
        self.data.is_empty()
    }

    fn size(&self) -> usize {
        self.data.len()
    }

    fn get_data(&self, py: Python) -> PyResult<Vec<(PyObject, PyObject)>> {
        Ok(self.data.iter().map(|(k, v)| (k.0.clone_ref(py), v.clone_ref(py))).collect())
    }

    fn set_data(&mut self, new_data: Vec<(PyObject, PyObject)>) {
        self.data = new_data.into_iter().map(|(k, v)| (PyObjectOrd(k), v)).collect();
    }
}

// ----------------- RustPriorityQueue -----------------

#[pyclass]
struct RustPriorityQueue {
    data: Vec<PyObjectOrd>,
    comparator: String,
}

#[pymethods]
impl RustPriorityQueue {
    #[new]
    fn new(comparator: Option<String>) -> Self {
        RustPriorityQueue {
            data: Vec::new(),
            comparator: comparator.unwrap_or_else(|| "max".to_string()),
        }
    }

    fn push(&mut self, value: PyObject) {
        self.data.push(PyObjectOrd(value));
        self.sift_up(self.data.len() - 1);
    }

    fn pop(&mut self) -> PyResult<()> {
        if !self.data.is_empty() {
            let last_idx = self.data.len() - 1;
            self.data.swap(0, last_idx);
            self.data.pop();
            if !self.data.is_empty() {
                self.sift_down(0);
            }
        }
        Ok(())
    }

    fn top(&self, py: Python) -> PyResult<Option<PyObject>> {
        if self.data.is_empty() {
            Ok(None)
        } else {
            Ok(Some(self.data[0].0.clone_ref(py)))
        }
    }

    fn empty(&self) -> bool {
        self.data.is_empty()
    }

    fn size(&self) -> usize {
        self.data.len()
    }

    fn get_data(&self, py: Python) -> PyResult<Vec<PyObject>> {
        Ok(self.data.iter().map(|x| x.0.clone_ref(py)).collect())
    }

    fn set_data(&mut self, new_data: Vec<PyObject>) {
        self.data = new_data.into_iter().map(PyObjectOrd).collect();
    }
}

impl RustPriorityQueue {
    fn sift_up(&mut self, mut idx: usize) {
        while idx > 0 {
            let parent = (idx - 1) / 2;
            if self.is_higher_priority(&self.data[idx], &self.data[parent]) {
                self.data.swap(idx, parent);
                idx = parent;
            } else {
                break;
            }
        }
    }

    fn sift_down(&mut self, mut idx: usize) {
        let len = self.data.len();
        loop {
            let left = 2 * idx + 1;
            let right = 2 * idx + 2;
            let mut highest = idx;

            if left < len && self.is_higher_priority(&self.data[left], &self.data[highest]) {
                highest = left;
            }
            if right < len && self.is_higher_priority(&self.data[right], &self.data[highest]) {
                highest = right;
            }

            if highest != idx {
                self.data.swap(idx, highest);
                idx = highest;
            } else {
                break;
            }
        }
    }

    fn is_higher_priority(&self, a: &PyObjectOrd, b: &PyObjectOrd) -> bool {
        if self.comparator == "min" {
            a < b
        } else {
            a > b
        }
    }
}

// ----------------- Bubble Sort Benchmark -----------------

#[pyfunction]
fn bubble_sort(mut arr: Vec<i32>) -> PyResult<Vec<i32>> {
    let len = arr.len();
    if len > 0 {
        for i in 0..len {
            for j in 0..len - 1 - i {
                if arr[j] > arr[j + 1] {
                    arr.swap(j, j + 1);
                }
            }
        }
    }
    Ok(arr)
}

// ----------------- C++ STL Algorithms -----------------

fn pyobject_lt(py: Python, a: &PyObject, b: &PyObject) -> PyResult<bool> {
    let a_bound = a.bind(py);
    let b_bound = b.bind(py);
    if let (Ok(x), Ok(y)) = (a_bound.extract::<i64>(), b_bound.extract::<i64>()) {
        return Ok(x < y);
    }
    if let (Ok(x), Ok(y)) = (a_bound.extract::<f64>(), b_bound.extract::<f64>()) {
        return Ok(x < y);
    }
    if let (Ok(x), Ok(y)) = (a_bound.extract::<&str>(), b_bound.extract::<&str>()) {
        return Ok(x < y);
    }
    a_bound.lt(b_bound)
}

fn pyobject_gt(py: Python, a: &PyObject, b: &PyObject) -> PyResult<bool> {
    let a_bound = a.bind(py);
    let b_bound = b.bind(py);
    if let (Ok(x), Ok(y)) = (a_bound.extract::<i64>(), b_bound.extract::<i64>()) {
        return Ok(x > y);
    }
    if let (Ok(x), Ok(y)) = (a_bound.extract::<f64>(), b_bound.extract::<f64>()) {
        return Ok(x > y);
    }
    if let (Ok(x), Ok(y)) = (a_bound.extract::<&str>(), b_bound.extract::<&str>()) {
        return Ok(x > y);
    }
    a_bound.gt(b_bound)
}

fn pyobject_eq(py: Python, a: &PyObject, b: &PyObject) -> PyResult<bool> {
    let a_bound = a.bind(py);
    let b_bound = b.bind(py);
    if let (Ok(x), Ok(y)) = (a_bound.extract::<i64>(), b_bound.extract::<i64>()) {
        return Ok(x == y);
    }
    if let (Ok(x), Ok(y)) = (a_bound.extract::<f64>(), b_bound.extract::<f64>()) {
        return Ok(x == y);
    }
    if let (Ok(x), Ok(y)) = (a_bound.extract::<&str>(), b_bound.extract::<&str>()) {
        return Ok(x == y);
    }
    a_bound.eq(b_bound)
}

#[pyfunction]
fn next_permutation(py: Python, arr: &Bound<'_, PyList>) -> PyResult<bool> {
    let mut vec: Vec<PyObject> = arr.extract()?;
    if vec.len() <= 1 {
        return Ok(false);
    }
    
    let mut i = vec.len() - 2;
    let mut found = false;
    loop {
        let current = &vec[i];
        let next = &vec[i + 1];
        if pyobject_lt(py, current, next).unwrap_or(false) {
            found = true;
            break;
        }
        if i == 0 {
            break;
        }
        i -= 1;
    }
    
    if !found {
        vec.reverse();
        for (idx, val) in vec.iter().enumerate() {
            arr.set_item(idx, val)?;
        }
        return Ok(false);
    }
    
    let mut j = vec.len() - 1;
    while j > i {
        if pyobject_gt(py, &vec[j], &vec[i]).unwrap_or(false) {
            break;
        }
        j -= 1;
    }
    
    vec.swap(i, j);
    vec[i + 1..].reverse();
    
    for (idx, val) in vec.iter().enumerate() {
        arr.set_item(idx, val)?;
    }
    
    Ok(true)
}

#[pyfunction]
fn prev_permutation(py: Python, arr: &Bound<'_, PyList>) -> PyResult<bool> {
    let mut vec: Vec<PyObject> = arr.extract()?;
    if vec.len() <= 1 {
        return Ok(false);
    }
    
    let mut i = vec.len() - 2;
    let mut found = false;
    loop {
        let current = &vec[i];
        let next = &vec[i + 1];
        if pyobject_gt(py, current, next).unwrap_or(false) {
            found = true;
            break;
        }
        if i == 0 {
            break;
        }
        i -= 1;
    }
    
    if !found {
        vec.reverse();
        for (idx, val) in vec.iter().enumerate() {
            arr.set_item(idx, val)?;
        }
        return Ok(false);
    }
    
    let mut j = vec.len() - 1;
    while j > i {
        if pyobject_lt(py, &vec[j], &vec[i]).unwrap_or(false) {
            break;
        }
        j -= 1;
    }
    
    vec.swap(i, j);
    vec[i + 1..].reverse();
    
    for (idx, val) in vec.iter().enumerate() {
        arr.set_item(idx, val)?;
    }
    
    Ok(true)
}

#[pyfunction]
fn nth_element(_py: Python, arr: &Bound<'_, PyList>, nth: usize) -> PyResult<()> {
    let mut vec: Vec<PyObject> = arr.extract()?;
    let len = vec.len();
    if nth < len {
        quickselect(&mut vec, 0, len - 1, nth);
        for (i, val) in vec.iter().enumerate() {
            arr.set_item(i, val)?;
        }
    }
    Ok(())
}

fn quickselect(arr: &mut Vec<PyObject>, left: usize, right: usize, nth: usize) {
    if left >= right {
        return;
    }
    let pivot_idx = partition_q(arr, left, right);
    if pivot_idx == nth {
        return;
    } else if pivot_idx > nth {
        if pivot_idx > 0 {
            quickselect(arr, left, pivot_idx - 1, nth);
        }
    } else {
        quickselect(arr, pivot_idx + 1, right, nth);
    }
}

fn partition_q(arr: &mut Vec<PyObject>, left: usize, right: usize) -> usize {
    let pivot_idx = left + (right - left) / 2;
    arr.swap(pivot_idx, right);
    let mut i = left;
    Python::with_gil(|py| {
        let pivot_val = arr[right].clone_ref(py);
        for j in left..right {
            if pyobject_lt(py, &arr[j], &pivot_val).unwrap_or(false) {
                arr.swap(i, j);
                i += 1;
            }
        }
    });
    arr.swap(i, right);
    i
}

#[pyfunction]
fn partition(py: Python, arr: &Bound<'_, PyList>, predicate: PyObject) -> PyResult<usize> {
    let mut vec: Vec<PyObject> = arr.extract()?;
    let mut i = 0;
    for j in 0..vec.len() {
        let val = vec[j].clone_ref(py);
        let is_true: bool = predicate.call1(py, (val,))?.extract(py)?;
        if is_true {
            vec.swap(i, j);
            i += 1;
        }
    }
    for (idx, val) in vec.iter().enumerate() {
        arr.set_item(idx, val)?;
    }
    Ok(i)
}

fn lower_bound_impl(py: Python, vec: &[PyObject], val: &PyObject, comp: &Option<PyObject>) -> PyResult<usize> {
    let mut left = 0;
    let mut right = vec.len();
    
    while left < right {
        let mid = left + (right - left) / 2;
        let mid_val = &vec[mid];
        
        let is_less = match comp {
            Some(c) => {
                let mid_obj = mid_val.clone_ref(py);
                let res: bool = c.call1(py, (mid_obj, val.clone_ref(py)))?.extract(py)?;
                res
            }
            None => {
                pyobject_lt(py, mid_val, val)?
            }
        };
        
        if is_less {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    Ok(left)
}

fn upper_bound_impl(py: Python, vec: &[PyObject], val: &PyObject, comp: &Option<PyObject>) -> PyResult<usize> {
    let mut left = 0;
    let mut right = vec.len();
    
    while left < right {
        let mid = left + (right - left) / 2;
        let mid_val = &vec[mid];
        
        let is_less = match comp {
            Some(c) => {
                let mid_obj = mid_val.clone_ref(py);
                let res: bool = c.call1(py, (val.clone_ref(py), mid_obj))?.extract(py)?;
                res
            }
            None => {
                pyobject_lt(py, val, mid_val)?
            }
        };
        
        if is_less {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    Ok(left)
}

#[pyfunction]
fn lower_bound(py: Python, arr: &Bound<'_, PyList>, val: PyObject, comp: Option<PyObject>) -> PyResult<usize> {
    let vec: Vec<PyObject> = arr.extract()?;
    lower_bound_impl(py, &vec, &val, &comp)
}

#[pyfunction]
fn upper_bound(py: Python, arr: &Bound<'_, PyList>, val: PyObject, comp: Option<PyObject>) -> PyResult<usize> {
    let vec: Vec<PyObject> = arr.extract()?;
    upper_bound_impl(py, &vec, &val, &comp)
}

#[pyfunction]
fn binary_search(py: Python, arr: &Bound<'_, PyList>, val: PyObject, comp: Option<PyObject>) -> PyResult<bool> {
    let vec: Vec<PyObject> = arr.extract()?;
    let len = vec.len();
    if len == 0 {
        return Ok(false);
    }
    let idx = lower_bound_impl(py, &vec, &val, &comp)?;
    if idx < len {
        let elem = &vec[idx];
        let eq = match &comp {
            Some(c) => {
                let elem_obj = elem.clone_ref(py);
                let less1: bool = c.call1(py, (elem_obj.clone(), val.clone_ref(py)))?.extract(py)?;
                let less2: bool = c.call1(py, (val.clone_ref(py), elem_obj))?.extract(py)?;
                !less1 && !less2
            }
            None => {
                pyobject_eq(py, elem, &val)?
            }
        };
        Ok(eq)
    } else {
        Ok(false)
    }
}

#[pyfunction]
fn equal_range(py: Python, arr: &Bound<'_, PyList>, val: PyObject, comp: Option<PyObject>) -> PyResult<(usize, usize)> {
    let vec: Vec<PyObject> = arr.extract()?;
    let lb = lower_bound_impl(py, &vec, &val, &comp)?;
    let ub = upper_bound_impl(py, &vec, &val, &comp)?;
    Ok((lb, ub))
}

// ----------------- Module Registration -----------------

#[pymodule]
fn _rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<RustStack>()?;
    m.add_class::<RustQueue>()?;
    m.add_class::<RustVector>()?;
    m.add_class::<RustSet>()?;
    m.add_class::<RustMap>()?;
    m.add_class::<RustPriorityQueue>()?;
    m.add_function(wrap_pyfunction!(bubble_sort, m)?)?;
    m.add_function(wrap_pyfunction!(next_permutation, m)?)?;
    m.add_function(wrap_pyfunction!(prev_permutation, m)?)?;
    m.add_function(wrap_pyfunction!(nth_element, m)?)?;
    m.add_function(wrap_pyfunction!(partition, m)?)?;
    m.add_function(wrap_pyfunction!(lower_bound, m)?)?;
    m.add_function(wrap_pyfunction!(upper_bound, m)?)?;
    m.add_function(wrap_pyfunction!(binary_search, m)?)?;
    m.add_function(wrap_pyfunction!(equal_range, m)?)?;
    Ok(())
}
