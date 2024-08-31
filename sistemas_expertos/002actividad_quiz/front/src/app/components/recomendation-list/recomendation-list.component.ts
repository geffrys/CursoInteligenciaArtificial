import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-recomendation-list',
  templateUrl: './recomendation-list.component.html',
  styleUrls: ['./recomendation-list.component.css']
})
export class RecomendationListComponent {
  @Input() recomendations: any[] = [];


}
