from odoo import models, fields, api
# from num2words import num2words


class AccountMove(models.Model):
    _inherit = 'account.move'

    # amount_in_words = fields.Char(
    #     string='Amount in Words',
    #     compute='_compute_amount_in_words_custom'
    # )

    # @api.depends('amount_total')
    # def _compute_amount_in_words_custom(self):
    #     for move in self:
    #         if move.amount_total:
    #             try:
    #                 # Using en_IN for South Asian numbering system (Lakh/Crore)
    #                 words = num2words(move.amount_total, lang='en_IN')
    #                 move.amount_in_words = words.upper()
    #             except NotImplementedError:
    #                 move.amount_in_words = str(move.amount_total)
    #         else:
    #             move.amount_in_words = ""

    amount_total_words_pkr = fields.Char(
        string='Amount in Words (PKR)',
        compute='_compute_amount_total_words_pkr'
    )

    @api.depends('amount_total')
    def _compute_amount_total_words_pkr(self):
        for move in self:
            move.amount_total_words_pkr = move.company_id.currency_id.amount_to_text(move.amount_total or 0.0)
