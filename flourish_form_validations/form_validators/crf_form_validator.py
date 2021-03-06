from django import forms


class CRFFormValidator:

    def clean(self):
        self.validate_against_visit_datetime(
            self.cleaned_data.get('report_datetime'))
        super().clean()

    def validate_against_visit_datetime(self, report_datetime):
        if (report_datetime and report_datetime <
                self.cleaned_data.get('maternal_visit').report_datetime):
            raise forms.ValidationError(
                "Report datetime cannot be before visit datetime.")

    # def validate_offstudy_model(self):
    #     maternal_offstudy_cls = django_apps.get_model(
    #         'td_prn.maternaloffstudy')
    #     action_cls = site_action_items.get(
    #         maternal_offstudy_cls.action_name)
    #     action_item_model_cls = action_cls.action_item_model_cls()
    #
    #     try:
    #         action_item_model_cls.objects.get(
    #             subject_identifier=self.subject_identifier,
    #             action_type__name=MATERNALOFF_STUDY_ACTION,
    #             status=NEW)
    #     except action_item_model_cls.DoesNotExist:
    #         try:
    #             maternal_offstudy_cls.objects.get(
    #                 subject_identifier=self.subject_identifier)
    #         except maternal_offstudy_cls.DoesNotExist:
    #             pass
    #         else:
    #             raise forms.ValidationError(
    #                 'Participant has been taken offstudy. Cannot capture any '
    #                 'new data.')
    #     else:
    #         self.maternal_visit = self.cleaned_data.get('maternal_visit') or None
    #         if not self.maternal_visit or self.maternal_visit.require_crfs == NO:
    #             raise forms.ValidationError(
    #                 'Participant is scheduled to be taken offstudy without '
    #                 'any new data collection. Cannot capture any new data.')
    #
