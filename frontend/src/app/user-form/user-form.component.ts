import { Component } from '@angular/core';
import { FormService } from '../form.service';

@Component({
  selector: 'app-user-form',
  template: `
    <div class="form-container">
      <form (ngSubmit)="onSubmit()">
        <div class="form-group">
          <label for="name">Name:</label>
          <input type="text" id="name" [(ngModel)]="formData.name" name="name" required>
        </div>

        <div class="form-group">
          <label for="email">Email:</label>
          <input type="email" id="email" [(ngModel)]="formData.email" name="email" required>
        </div>

        <div class="form-group">
          <label for="numCredits">Number of HUB credits desired:</label>
          <select [(ngModel)]="formData.numCredits" name="numCredits">
            @for(val of creditOptions; track val) {
              <option value={{val}}>{{ val }}</option>
            }
          </select>
        </div>

        <div class="form-group">
          <label for="desiredHubs">Choose the HUBs you need:</label>
          <select multiple [(ngModel)]="formData.desiredHubs" name="desiredHubs">
            @for(hub of hubOptions; track hub) {
              <option value={{hub}}>{{ hub }}</option>
            }
          </select>
        </div>

        <button type="submit" class="submit-button">Submit</button>
      </form>
    </div>
  `,
  styleUrls: ['./user-form.component.css']
})
export class UserFormComponent {
  formData = { name: '', email: '' , numCredits: '', desiredHubs: ''};
  // desiredHubs = new FormControl('');
  hubOptions: string[] = ['Aesthetic Exploration', 'Creativity/Innovation', 'Critical Thinking', 'Digitial/Multimedia', 
  'Ethical Reasoning', 'First-Year Writing Seminar', 'Global Citizenship', 'Historical Consciousness', 'Oral/Signed Communication',
  'Philosophical Inquiry', 'Quantitative Reasoning I', 'Quantitative Reasoning II', 'Research and Information', 'Scientific Inquiry I',
  'Scientific Inquiry II', 'Teamwork/Collaboration', 'Writing, Research, Inquiry', 'Writing-Intensive Course'];
  creditOptions: number[] = [4, 8, 12, 16, 20];

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

