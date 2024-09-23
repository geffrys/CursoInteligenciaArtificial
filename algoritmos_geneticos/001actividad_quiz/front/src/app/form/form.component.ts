import { Component, OnInit } from '@angular/core';
import { ApiConsumeService } from '../services/api-consume.service';

@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.css']
})
export class FormComponent implements OnInit{

  constructor(private api:ApiConsumeService) { }

  genres: any;
  moods: any;

  onSubmit(data: any){
    console.log(data);
  }

  ngOnInit(): void {
    this.api.getMoods().forEach((data: any) => {
      console.log(data);
      this.moods = data;
    }, );
    this.api.getGenres().forEach((data: any) => {
      console.log(data);
      this.genres = data;
    }, );
  }

}
