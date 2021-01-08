mkdir -p build
cd build

[ -d opencv ] || git clone https://github.com/opencv/opencv.git
[ -d opencv_contrib ] || git clone https://github.com/opencv/opencv_contrib.git

docker run --rm --workdir /src -v $(pwd):/src emscripten/emsdk emcmake python3 opencv/platforms/js/build_js.py build_js  --cmake_option="-DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib/modules"

cp build_js/bin/opencv.js ..
