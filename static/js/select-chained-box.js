SelectChainedBox = function (params) {

    var $select = params.$select,
        $target = params.$target,
        value = String(params.value),
        isReversed = Boolean(params.isReversed);

    function isVisible() {
        var currentValue = $select.val();

        if ($select.prop('multiple')) {
            return currentValue && $.inArray(value, currentValue) !== -1;
        }

        return currentValue == value;
    }

    function refresh() {
        var isShown = isVisible();

        if (isReversed) {
            isShown = !isShown;
        }

        $target.toggle(isShown);
    }

    $select.on('change', refresh);

    refresh();
};