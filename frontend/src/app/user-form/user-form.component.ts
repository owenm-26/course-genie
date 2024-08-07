import { Component } from '@angular/core';
import { FormService } from '../form.service';

@Component({
  selector: 'app-user-form',
  templateUrl: './user-form.component.html',
  styleUrls: ['./user-form.component.css']
})
export class UserFormComponent {
  formData = { name: '', email: '' , numCredits: '', desiredHubs: ''};
  // desiredHubs = new FormControl('');
  hubOptions: string[] = ['Aesthetic Exploration', 'Creativity/Innovation', 'Critical Thinking', 'Digitial/Multimedia', 
  'Ethical Reasoning', 'First-Year Writing Seminar', 'Global Citizenship', 'Historical Consciousness', 'Oral/Signed Communication',
  'Philosophical Inquiry', 'Quantitative Reasoning I', 'Quantitative Reasoning II', 'Research and Information', 'Scientific Inquiry I',
  'Scientific Inquiry II', 'Teamwork/Collaboration', 'Writing, Research, Inquiry', 'Writing-Intensive Course'];

  constructor(private formService: FormService) {}

  onSubmit() {
    this.formService.submitForm(this.formData)
      .subscribe(response => {
        console.log('Server response:', response);
      }, error => {
        console.error('Error:', error);
      });
  }
}

