import { PrincipalService } from './../../services/principal/principal.service';
import { Operation } from './../../models/Operation';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormArray, FormControl, Validators, AbstractControl } from '@angular/forms';
@Component({
  selector: 'app-principal',
  templateUrl: './principal.component.html',
  styleUrls: ['./principal.component.scss']
})
export class PrincipalComponent implements OnInit {

  Data: Array<any> = [
  { name: 'Tokenization', value: 'Tokenization' },
  { name: 'Stop Words' , value: 'Stop Words' },
  { name: 'Lemmatization', value: 'Lemmatization' },
  { name: 'Stemming', value: 'Stemming' },
  { name: 'Pos Tagging', value: 'Pos Tagging' },
  { name: 'Bag Of Words', value: 'Bag Of Words' },
  { name: 'TF-IDF', value: 'TF-IDF'},
  { name: 'Word2Vec', value: 'Word2Vec' }
 ];

 form: FormGroup;
 serv: String = "";

  constructor(private fb: FormBuilder, private principalService: PrincipalService) {
  this.form = this.fb.group({
    checkArray: this.fb.array([]),
    myText: new FormControl('', Validators.required)
  })
}

  ngOnInit(): void {


  }

  onCheckboxChange(e: any) {
    const checkArray: FormArray = this.form.get('checkArray') as FormArray;

    if (e.target.checked) {
      checkArray.push(new FormControl(e.target.value));
    } else {
      let i: number = 0;
      checkArray.controls.forEach((item: AbstractControl) => {
        if (item.value == e.target.value) {
          checkArray.removeAt(i);
          return;
        }
        i++;
      });
    }
  }

  submitForm() {

    for (var val of this.form.value.checkArray)
    {
      // this.serv += val
      // this.serv += "-"
      this.serv = val
    }

    this.principalService.add(this.form)

  }



}
