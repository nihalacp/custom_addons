odoo.define('custom_widget.ColorPickerWidget', function (require) {
    "use strict";

    var AbstractField = require('web.AbstractField');
    var fieldRegistry = require('web.field_registry');

    var ColorPickerWidget = AbstractField.extend({
        supportedFieldTypes: ['char'],  // The widget is applied to char fields

        // Rendering the color picker input field
        _render: function () {
            var self = this;
            this.$el.html('<input type="color" class="o_field_color_picker" value="' + this.value + '"/>');
            this.$('input').on('change', function () {
                self._setValue($(this).val());  // Update the field value when the color changes
            });
        },
    });

    // Register the widget so that it can be used in views
    fieldRegistry.add('color_picker', ColorPickerWidget);
});
